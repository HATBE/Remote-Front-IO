const btnPower = document.getElementById('btnPower');
const btnPowerhard = document.getElementById('btnPowerhard');
const btnReset = document.getElementById('btnReset');
const led = document.getElementById('led');

const pcStates = {ukn: {text: 'UKN', class: 'ukn'}, on: {text: 'ON', class: 'on'}, off: {text: 'OFF', class: 'off'}}

let state = pcStates.ukn;

function init() {
    setLed(state);
}

function setLed(s) {
    disableLed();
    led.classList.add(s.class);
    led.textContent = s.text;
}

function disableLed() {
    led.classList.remove('on', 'off', 'ukn');
}

function updateLed() {
    $.get('./pcState.json', (data) => {
        if(data == null) {
            alert('Sorry, no data found');
            return;
        }
        state = data.state == 1 ? pcStates.on : pcStates.off;
        setLed(state);
    })
    .fail(() => {
        alert('Sorry, no data found');
        return;
    });
}

function updateUi() {
    updateLed();
}

function pressPower() {
    disenableBtns(1000);
    $.post('./action.php', {action: 'power'});
}

function pressPowerhard() {
    disenableBtns(5000);
    $.post('./action.php', {action: 'powerhard'});
}

function pressReset() {
    disenableBtns(1000);
    $.post('./action.php', {action: 'reset'});
}

function disenableBtns(ms) {
    btnPower.disabled = true;
    btnPowerhard.disabled = true;
    btnReset.disabled = true;
    setTimeout(() => {
        btnPower.disabled = false;
        btnPowerhard.disabled = false;
        btnReset.disabled = false;
    }, ms);
}

init();
updateUi(); setInterval(() => {updateUi()}, 1000);

btnPower.addEventListener('click', () => {pressPower()});
btnPowerhard.addEventListener('click', () => {pressPowerhard()});
btnReset.addEventListener('click', () => {pressReset()});
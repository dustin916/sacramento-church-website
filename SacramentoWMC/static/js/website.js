/* Time */
const timeControl = document.querySelector('input[type="time"]');
timeControl.value = '15:30';

const startTime = document.getElementById("startTime");
const valueSpan = document.getElementById("value");

startTime.addEventListener('input[type="time"]', () => {
  valueSpan.innerText = startTime.value;
}, false)


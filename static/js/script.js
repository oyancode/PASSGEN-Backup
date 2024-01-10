let i = 0;
const text = "PASSWORD GENERATOR";
const speed = 60; 

function typeWriter() {
  if (i < text.length) {
    document.querySelector("h1").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

window.onload = function () {
  document.querySelector("h1").innerHTML = ""; 
  typeWriter(); 
};
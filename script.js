function updateFontSize() {
    let caption = document.getElementById('caption');
    let newSize = prompt("Enter new font size (e.g., 30px):");
    caption.style.fontSize = newSize;
}

function updateColor() {
    let caption = document.getElementById('caption');
    let newColor = prompt("Enter new color (e.g., blue):");
    caption.style.color = newColor;
}

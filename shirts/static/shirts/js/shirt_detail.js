
function showSize(ln) {
    // Show available sizes for particular material
    console.log()
    for (let i=1; i <= ln; i++) {
        let sizes = document.getElementById("szs" + i);
        let material = document.getElementById("mtr" + i);

        if (material.checked) {
            sizes.style.display = "block";
        } else {
            sizes.style.display = "none";
        }
    }
}

window.onload = showSize('{{materials|length}}');
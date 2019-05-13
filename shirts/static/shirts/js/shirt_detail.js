
let sizes = document.querySelector(".sizes")

function showSize(ln) {
    // Show available sizes for particular material
    console.log()
    for (let i=1; i <= ln; i++) {
        let size = document.getElementById("sz" + i);
        let material = document.getElementById("mtr" + i);

        console.log(size);
        if (size.checked) {
            console.log('checked ');
            // i += 1
            material.style.display = "block";
        } else {
            console.log('not checked ')
            material.style.display = "none";
        }
    }
}


// sizes.addEventListener("input", showSize(ln))
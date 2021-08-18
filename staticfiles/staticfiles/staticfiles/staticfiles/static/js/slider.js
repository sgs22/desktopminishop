let thumbnails = document.getElementsByClassName('thumbnail')

let activeImages = document.getElementsByClassName('active')

for (var i=0; i < thumbnails.length; i++) {
    thumbnails[i].addEventListener('mousedown', function() {
        if (activeImages.length > 0) {
            activeImages[0].classList.remove('active')
        }
        this.classList.add('active')
        document.getElementById('featured').src = this.src
    })
}

const buttonLeft = document.getElementById('slideLeft');
const buttonRight = document.getElementById('slideRight');

buttonLeft.addEventListener('click', function() {
    document.getElementById('slider').scrollLeft -= 400
})
buttonRight.addEventListener('click', function() {
    document.getElementById('slider').scrollLeft += 400
})

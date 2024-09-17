// Function to initialize and handle a slider
function initializeSlider(sliderId) {
    let items = document.querySelectorAll(`#${sliderId} .item`);
    let next = document.getElementById(`next-${sliderId}`);
    let prev = document.getElementById(`prev-${sliderId}`);
    
    let active = 0;

    function loadShow() {
        let stt = 0;
        items[active].style.transform = `none`;
        items[active].style.zIndex = 1;
        items[active].style.filter = 'none';
        items[active].style.opacity = 1;
        
        // Process items after the active one
        for (let i = active + 1; i < items.length; i++) {
            stt++;
            items[i].style.transform = `translateX(${120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(-1deg)`;
            items[i].style.zIndex = -stt;
            items[i].style.filter = 'blur(5px)';
            items[i].style.opacity = stt > 2 ? 0 : 0.6;
        }
        
        stt = 0;
        
        // Process items before the active one
        for (let i = active - 1; i >= 0; i--) {
            stt++;
            items[i].style.transform = `translateX(${-120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(1deg)`;
            items[i].style.zIndex = -stt;
            items[i].style.filter = 'blur(5px)';
            items[i].style.opacity = stt > 2 ? 0 : 0.6;
        }
    }

    loadShow();

    // Handle touch events
    let startX, endX;
    const swipeThreshold = 50; // Minimum distance to detect a swipe

    function handleTouchStart(event) {
        startX = event.touches[0].clientX;
    }

    function handleTouchMove(event) {
        endX = event.touches[0].clientX;
    }

    function handleTouchEnd() {
        if (startX - endX > swipeThreshold) {
            // Swiped left
            active = (active + 1 < items.length) ? active + 1 : active;
            loadShow();
        } else if (endX - startX > swipeThreshold) {
            // Swiped right
            active = (active - 1 >= 0) ? active - 1 : active;
            loadShow();
        }
    }

    const sliderElement = document.getElementById(sliderId);
    sliderElement.addEventListener('touchstart', handleTouchStart);
    sliderElement.addEventListener('touchmove', handleTouchMove);
    sliderElement.addEventListener('touchend', handleTouchEnd);

    // Handle button clicks if they are present
    if (next && prev) {
        next.onclick = function() {
            active = (active + 1 < items.length) ? active + 1 : active;
            loadShow();
        };

        prev.onclick = function() {
            active = (active - 1 >= 0) ? active - 1 : active;
            loadShow();
        };
    }
}

// Initialize both sliders
initializeSlider('certifications-slider');
initializeSlider('tools-slider');



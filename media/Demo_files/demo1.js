document.addEventListener("DOMContentLoaded", function() {
    // Certifications Slider
    const certificationsSlider = document.getElementById('certifications-slider');
    const certificationsItemsWrapper = certificationsSlider.querySelector('.items-wrapper');
    const prevCertificationsButton = document.getElementById('prev-certifications-slider');
    const nextCertificationsButton = document.getElementById('next-certifications-slider');

    // Tools Slider
    const toolsSlider = document.getElementById('tools-slider');
    const toolsItemsWrapper = toolsSlider.querySelector('.items-wrapper');
    const prevToolsButton = document.getElementById('prev-tools-slider');
    const nextToolsButton = document.getElementById('next-tools-slider');

    const updateSlider = (slider, itemsWrapper, direction) => {
        const itemWidth = slider.querySelector('.item').offsetWidth + 20; // Width of items including margin
        const maxIndex = itemsWrapper.children.length - Math.floor(slider.offsetWidth / itemWidth);
        let currentIndex = parseInt(itemsWrapper.style.transform.replace(/[^\d]/g, '') || 0, 10) / itemWidth || 0;

        if (direction === 'next') {
            currentIndex = Math.min(currentIndex + 1, maxIndex);
        } else {
            currentIndex = Math.max(currentIndex - 1, 0);
        }

        itemsWrapper.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
    };

    prevCertificationsButton.addEventListener('click', () => {
        updateSlider(certificationsSlider, certificationsItemsWrapper, 'prev');
    });

    nextCertificationsButton.addEventListener('click', () => {
        updateSlider(certificationsSlider, certificationsItemsWrapper, 'next');
    });

    prevToolsButton.addEventListener('click', () => {
        updateSlider(toolsSlider, toolsItemsWrapper, 'prev');
    });

    nextToolsButton.addEventListener('click', () => {
        updateSlider(toolsSlider, toolsItemsWrapper, 'next');
    });
});

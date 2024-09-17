document.addEventListener('DOMContentLoaded', function () {
    const lists = document.querySelectorAll('.content-certificates, .content-tools');
    let listIndex = 0;

    function showNextItem() {
        if (listIndex < lists.length) {
            const listItems = lists[listIndex].querySelectorAll('.typing-container');
            let itemIndex = 0;

            function showNextItemInList() {
                if (itemIndex < listItems.length) {
                    const currentItem = listItems[itemIndex];
                    
                    // Reset animation
                    currentItem.classList.remove('typing');
                    void currentItem.offsetWidth; // Trigger reflow
                    currentItem.classList.add('typing');

                    // Show the current item with typing effect
                    currentItem.classList.add('visible');
                    currentItem.classList.remove('hidden');

                    // Calculate the duration of the typing animation
                    const typingDuration = 50; // Adjust this duration as needed

                    // Proceed to the next item after typing animation completes
                    setTimeout(() => {
                        itemIndex++;
                        showNextItemInList();
                    }, typingDuration + 100); // Add extra time before showing the next item
                } else {
                    // Move to the next list after all items in the current list have been shown
                    listIndex++;
                    // Start the next list after a delay
                    setTimeout(showNextItem, 100); // Delay before moving to the next list
                }
            }

            // Start showing items in the current list
            showNextItemInList();
        } else {
            // All lists processed
            console.log('All items have been processed.');
        }
    }

    // Initialize the animation
    showNextItem();
});

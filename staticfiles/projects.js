document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.project-column').forEach(column => {
      column.addEventListener('click', () => {
        column.classList.toggle('flipped');

        setTimeout(() => {
          column.classList.remove('flipped'); // Flip back to front after 3 seconds
          column.classList.add('flip-back');  // Trigger the back flip animation
        }, 3000); 
      });
    });
  });
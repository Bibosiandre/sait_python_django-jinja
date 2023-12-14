document.addEventListener('DOMContentLoaded', function() {
  const galleryImages = document.querySelectorAll('.gallery img');

  galleryImages.forEach(function(image) {
    image.addEventListener('click', function() {
      if (this.classList.contains('active')) {
        this.classList.remove('active');
        this.classList.remove('zoom');
      } else {
        this.classList.add('active');
        this.classList.add('zoom');
      }
    });
  });
});
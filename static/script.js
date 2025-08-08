// small UI helpers
document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.querySelector('input[type="file"]');
  const label = document.querySelector('.file-label span');

  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      const f = e.target.files[0];
      if (f) label.textContent = `${f.name} (${Math.round(f.size/1024)} KB)`;
      else label.textContent = 'Select image';
    });
  }
});

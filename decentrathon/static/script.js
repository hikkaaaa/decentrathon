const dropdown = document.getElementById('languageDropdown');
const button = document.getElementById('dropdownButton');
const content = document.getElementById('dropdownContent');
const selected = document.getElementById('selectedLang');

// Toggle dropdown visibility
button.addEventListener('click', () => {
  dropdown.classList.toggle('show');
});

// Change language on click
content.querySelectorAll('div').forEach(item => {
  item.addEventListener('click', () => {
    selected.textContent = item.dataset.lang;
    dropdown.classList.remove('show');
  });
});

document.addEventListener('click', (e) => {
    if (!dropdown.contains(e.target)) {
      dropdown.classList.remove('show');
    }
  })

  
document.getElementById("file-upload").addEventListener("change", function() {
    if (this.files.length > 0) {
        document.getElementById("predict-btn").style.display = "block";
    }
});
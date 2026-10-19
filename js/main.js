const menuBtn = document.getElementById('menuBtn');
const mainNav = document.getElementById('mainNav');
menuBtn.addEventListener('click', () => {
  const open = mainNav.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', open);
});

const copyBtn = document.getElementById('copyBtn');
if (copyBtn) {
  copyBtn.addEventListener('click', () => {
    const email = document.getElementById('email');
    navigator.clipboard.writeText(email.textContent)
      .then(() => { copyBtn.textContent = 'Copied'; })
      .catch(() => {
        const range = document.createRange();
        range.selectNodeContents(email);
        const sel = getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      });
  });
}

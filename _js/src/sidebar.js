// JavaScript for toggling the open class
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', function() {
        this.classList.toggle('open');
    });
});

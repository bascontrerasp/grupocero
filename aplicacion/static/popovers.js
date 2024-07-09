document.addEventListener("DOMContentLoaded", function() {
    var popovers = new bootstrap.Popover(document.body, {
        selector: '[data-bs-toggle="popover"]',
        trigger: 'hover'
    });
});

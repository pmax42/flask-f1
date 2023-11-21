// Close toast message
function closeToast() {
    const toasts = document.getElementsByClassName("toast");
    for (let toast of toasts) {
        const closeToastButton = toast.querySelector("#close-toast");
        closeToastButton.addEventListener("click", () => {
            toast.remove();
        });
        setTimeout(() => {
            toast.remove();
        }, 5000);
    };
}

window.onload = () => {
    closeToast();
}
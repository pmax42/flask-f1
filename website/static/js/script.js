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

// Get class color
window.getBgColorClassByConstructor = function(constructor){
    return "bg-" + constructor;
}
window.getHoverTextClassByConstructor = function(constructor){
    return "hover:text-" + constructor;
}
window.getHoverLiClassByConstructor = function(constructor){
    return "hover:border-" + constructor + " " + "hover:shadow-" + constructor + "/25";
}
window.getTextClassByConstructor = function(constructor){
    return "text-" + constructor;
}

window.onload = () => {
    closeToast();
}
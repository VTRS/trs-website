function yourFunction() {
    const hide = document.getElementById("hide");
    hide.className =
      hide.className === "hide"
        ? (hide.className = "example removeHide")
        : (hide.className = "hide");
    setTimeout(yourFunction, 1500);
}
yourFunction();
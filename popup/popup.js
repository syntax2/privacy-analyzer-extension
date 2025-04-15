// Reference to the container that displays trackers
const trackersDiv = document.getElementById("trackers");

// Clear the default "No trackers detected" message when the first tracker is added.
function clearPlaceholder() {
  if (
    trackersDiv.children.length === 1 &&
    trackersDiv.children[0].tagName === "P"
  ) {
    trackersDiv.innerHTML = "";
  }
}

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((msg) => {
  if (msg.type === "TRACKER_FOUND") {
    clearPlaceholder();

    // Create a new div to show tracker information.
    const trackerDiv = document.createElement("div");
    trackerDiv.textContent = `🛑 ${msg.tracker} on ${msg.page}`;

    // Append to the trackers container.
    trackersDiv.appendChild(trackerDiv);
  }
});

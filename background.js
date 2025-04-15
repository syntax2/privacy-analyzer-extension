// A simple in-memory storage of detected tracker domains.
// In a production extension, consider using chrome.storage for persistence.
let trackerList = new Set();

// Listen for completed web requests
chrome.webRequest.onCompleted.addListener(
  (details) => {
    try {
      const url = new URL(details.url);
      const domain = url.hostname;

      // Filter: For demonstration, only consider domains that are not the current domain.
      // In a real extension, you may add conditions to identify common tracker domains.
      if (!trackerList.has(domain)) {
        trackerList.add(domain);
        // Send a message with the tracker info
        chrome.runtime.sendMessage({
          type: "TRACKER_FOUND",
          tracker: domain,
          page: details.initiator || details.documentUrl || details.url,
        });
      }
    } catch (error) {
      console.error("Error processing URL: ", details.url, error);
    }
  },
  { urls: ["<all_urls>"] }
);

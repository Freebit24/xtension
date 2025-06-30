// Listen for a click on the extension icon in the toolbar.
// When clicked, open the extension's 'popup.html' page in a new browser tab.
chrome.action.onClicked.addListener(() => {
  chrome.tabs.create({
    url: chrome.runtime.getURL("popup.html")
  });
});

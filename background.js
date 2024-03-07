const extensionAPI = typeof browser === 'undefined' ? chrome : browser;


extensionAPI.runtime.onInstalled.addListener(function () {
    extensionAPI.contextMenus.create({
      title: "Summarize the text",
      contexts: ["selection"],
      id: "summarizeText"
    });
    extensionAPI.contextMenus.create({
      title: "Play the text",
      contexts: ["selection"],
      id: "playText"
    });
    extensionAPI.contextMenus.create({
        title: "Re translate to original",
        contexts: ["page"],
        id: "wrongText"
      });
  });
  
  extensionAPI.contextMenus.onClicked.addListener(function (info, tab) {
    if (info.menuItemId === "summarizeText") {
      extensionAPI.tabs.sendMessage(tab.id, { action: "reportText", selectedText: info.selectionText });
    }
    if (info.menuItemId === "playText") {
      extensionAPI.tabs.sendMessage(tab.id, { action: "playText", selectedText: info.selectionText });
    }
    if (info.menuItemId === "wrongText") {
        extensionAPI.tabs.sendMessage(tab.id, { action: "wrongText" });
      }
  });
  
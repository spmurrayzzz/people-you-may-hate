chrome.extension.sendMessage({}, function(response) {
	var readyStateCheckInterval = setInterval(function() {
		if (document.readyState === "complete") {
			clearInterval(readyStateCheckInterval);
			
			var stupid_fb_thing = document.getElementById('pagelet_ego_pane_w');
			stupid_fb_thing.style.display = 'none';
		}
	}, 10);
});
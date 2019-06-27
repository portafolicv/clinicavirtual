var CACHE_NAME = 'clinica_nutricional_cache';
var urlsToCache = [
	'/myapp/home/',
	'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
	'https://use.fontawesome.com/releases/v5.5.0/css/all.css',
	'https://code.jquery.com/jquery-3.3.1.slim.min.js',
	'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js',
	'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js',
	'/static/css/custom.css',
];

self.addEventListener('install', function (event) {
	// Perform install steps
	event.waitUntil(
		caches.open(CACHE_NAME)
			.then(function (cache) {
				console.log('Opened cache');
				return cache.addAll(urlsToCache);
			})
	);
});

self.addEventListener('fetch', function(event) {
	event.respondWith(
		caches.match(event.request)
			.then(function(response) {
				// Cache hit - return response
				if (response) {
				return response;
				}
				return fetch(event.request);
			}
		)
	);
});


/*

self.addEventListener('fetch', function (event) {
	event.respondWith(
		caches.match(event.request)
			.then(function (response) {
				// Cache hit - return response
				if (response) {
					return response;
				}

				// IMPORTANT: Clone the request. A request is a stream and
				// can only be consumed once. Since we are consuming this
				// once by cache and once by the browser for fetch, we need
				// to clone the response.
				var fetchRequest = event.request.clone();

				return fetch(fetchRequest).then(
					function (response) {
						// Check if we received a valid response
					if (!response || response.status !== 200 || response.type !== 'basic') {
						return response;
					}

					// IMPORTANT: Clone the response. A response is a stream
					// and because we want the browser to consume the response
					// as well as the cache consuming the response, we need
					// to clone it so we have two streams.
					var responseToCache = response.clone();

					caches.open(CACHE_NAME)
						.then(function (cache) {
							cache.put(event.request, responseToCache);
						});

					return response;
				}
			);
		})
	);
});

*/
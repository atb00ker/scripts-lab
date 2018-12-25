//Latest CACHE_NAME
var CACHE_NAME = '[v0.1.0] ToC';


//Files to be Cached
var urlsToCache = [
    './index.html'
];


// Perform install steps
self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
            return cache.addAll(urlsToCache);
        }).catch(function (Error) {
            console.log(urlsToCache);
        })
    );
});

// Activation is done Everytime a page loads!
self.addEventListener('activate', function (event) {
    console.log('[ServiceWorker] Activated');
    event.waitUntil(
        caches.keys().then(function (keyList) {
            return Promise.all(keyList.map(function (key) {
                if (key !== CACHE_NAME) {
                    console.log('[ServiceWorker] Removing Obselete Cache: ', key);
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});


//Called Everytime a resource is needed!
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request, { ignoreSearch: true }).then(response => {
            return response || fetch(event.request);
        })
    );
});

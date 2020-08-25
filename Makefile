
.PHONY: serve
serve: python.localhost-key.pem
	python3 ./websocket-proxy.py

python.localhost-key.pem:
	mkcert python.localhost
	cat python.localhost.pem >> python.localhost-key.pem
	mkcert -install

.PHONY: clean
clean:
	rm -rf \
		python.localhost.pem \
		python.localhost-key.pem

REPO_ROOT := $(abspath .)
GENERATED_PYTHON_DIR := $(REPO_ROOT)/caikit_nlp_client/generated

.PHONY: generate_proto generate_python build clean clean-generated help integration-test test stop-test-server start-test-server

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

$(REPO_ROOT)/protobuf:
	mkdir -pv $(REPO_ROOT)/protobuf

generate-proto: $(REPO_ROOT)/protobuf ##Generate the .proto files from a running instance of caikit-nlp grpc server
	RUNTIME_LIBRARY=caikit_nlp python -m caikit.runtime.dump_services $(REPO_ROOT)/protobuf

clean: ##Clean the created artifacts
	rm -rf dist


build: ##Build the wheel
	poetry build

test:  ## Run unit tests / integration tests against a running server
	pytest --log-level=DEBUG tests

integration-test: start-test-server test stop-test-server ## Start a server, run the tests, stop the tests

start-test-server: ## Start the server
	@echo "Starting a server"
	docker-compose up -d
	sleep 30

stop-test-server: ## Stop the server
	@echo "Stopping the server"
	docker-compose logs
	docker-compose down

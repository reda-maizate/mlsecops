build-proc:
	sh scripts/build_and_push.sh face_spoofing_ecr docker/processing

build-train:
	sh scripts/build_and_push.sh face_spoofing_ecr_train docker/training

run-jobs:
	python3 scripts/run_jobs.py

man-mlflow-model:
	python3 scripts/manage_mlflow_model.py

dep-stack:
	sh scripts/deploy_stack.sh
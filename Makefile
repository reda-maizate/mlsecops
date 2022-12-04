build-proc:
	sh scripts/build_and_push.sh face_spoofing_ecr docker/processing

run-jobs:
	python3 scripts/run_jobs.py
#!/usr/bin/env bash
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

set -e

echo "This script checks of presence of variables required to perform operations on Google Cloud Platform. They should be stored as secrets."
echo "More detailed information about Google Cloud Platform Credentials can be found in CI.md"

function check_vars() {
  ret=true
  for var in "$@"; do
    if [ -n "${!var}" ]; then
      echo "$var is set"
    else
      echo >&2 "$var is not set"
      ret=false
    fi
  done
  $ret
}

if ! check_vars "GCP_PROJECT_ID" "GCP_REGION" "GCP_SA_EMAIL" "GCP_SA_KEY" "GCP_TESTING_BUCKET" "GCP_PYTHON_WHEELS_BUCKET"; then
  echo "gcp-variables-set=false" >> $GITHUB_OUTPUT
  echo >&2 "!!! WARNING !!!"
  echo >&2 "Not all GCP variables are set. Jobs which require them will be skipped."
else
  echo "gcp-variables-set=true" >> $GITHUB_OUTPUT
fi

/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.beam.sdk.io.fileschematransform;

import org.apache.beam.sdk.annotations.Internal;
import org.apache.beam.sdk.schemas.io.Providers;
import org.apache.beam.sdk.transforms.PTransform;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PDone;

/**
 * Provides a {@link PTransform} that consumes a {@link PCollection} according to a registered
 * {@link com.google.auto.service.AutoService} {@link FileWriteSchemaTransformFormatProvider}
 * implementation. See {@link FileWriteSchemaTransformFormatProviders} for a list of available
 * formats.
 */
@Internal
public interface FileWriteSchemaTransformFormatProvider extends Providers.Identifyable {

  /** Builds a {@link PTransform} that consumes {@link PCollection}. */
  PTransform<PCollection<?>, PDone> buildTransform();
}

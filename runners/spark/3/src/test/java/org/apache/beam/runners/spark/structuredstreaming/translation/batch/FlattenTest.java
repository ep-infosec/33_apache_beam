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
package org.apache.beam.runners.spark.structuredstreaming.translation.batch;

import java.io.Serializable;
import org.apache.beam.runners.spark.structuredstreaming.SparkStructuredStreamingPipelineOptions;
import org.apache.beam.runners.spark.structuredstreaming.SparkStructuredStreamingRunner;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.testing.PAssert;
import org.apache.beam.sdk.testing.TestPipeline;
import org.apache.beam.sdk.transforms.Create;
import org.apache.beam.sdk.transforms.Flatten;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PCollectionList;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/** Test class for beam to spark flatten translation. */
@RunWith(JUnit4.class)
public class FlattenTest implements Serializable {
  @Rule public transient TestPipeline pipeline = TestPipeline.fromOptions(testOptions());

  private static PipelineOptions testOptions() {
    SparkStructuredStreamingPipelineOptions options =
        PipelineOptionsFactory.create().as(SparkStructuredStreamingPipelineOptions.class);
    options.setRunner(SparkStructuredStreamingRunner.class);
    options.setTestMode(true);
    return options;
  }

  @Test
  public void testFlatten() {
    PCollection<Integer> input1 = pipeline.apply(Create.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
    PCollection<Integer> input2 = pipeline.apply(Create.of(11, 12, 13, 14, 15, 16, 17, 18, 19, 20));
    PCollectionList<Integer> pcs = PCollectionList.of(input1).and(input2);
    PCollection<Integer> input = pcs.apply(Flatten.pCollections());
    PAssert.that(input)
        .containsInAnyOrder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20);
    pipeline.run();
  }
}

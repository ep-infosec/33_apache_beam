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
package org.apache.beam.runners.spark.util;

import java.util.Collection;
import java.util.stream.Collectors;
import org.apache.beam.runners.core.TimerInternals;
import org.apache.beam.runners.spark.stateful.SparkTimerInternals;
import org.apache.beam.sdk.transforms.windowing.BoundedWindow;
import org.apache.beam.sdk.values.WindowingStrategy;

public class TimerUtils {

  public static <W extends BoundedWindow> void dropExpiredTimers(
      SparkTimerInternals sparkTimerInternals, WindowingStrategy<?, W> windowingStrategy) {
    Collection<TimerInternals.TimerData> expiredTimers =
        sparkTimerInternals.getTimers().stream()
            .filter(
                timer ->
                    timer
                        .getTimestamp()
                        .plus(windowingStrategy.getAllowedLateness())
                        .isBefore(sparkTimerInternals.currentInputWatermarkTime()))
            .collect(Collectors.toList());

    // Remove the expired timer from the timerInternals structure
    expiredTimers.forEach(sparkTimerInternals::deleteTimer);
  }
}

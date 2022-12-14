// Licensed to the Apache Software Foundation (ASF) under one or more
// contributor license agreements.  See the NOTICE file distributed with
// this work for additional information regarding copyright ownership.
// The ASF licenses this file to You under the Apache License, Version 2.0
// (the "License"); you may not use this file except in compliance with
// the License.  You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by starcgen. DO NOT EDIT.
// File: passert.shims.go

package passert

import (
	"context"
	"fmt"
	"io"
	"reflect"

	// Library imports
	"github.com/apache/beam/sdks/v2/go/pkg/beam/core/runtime"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/core/runtime/exec"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/core/runtime/graphx/schema"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/core/sdf"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/core/typex"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/core/util/reflectx"
)

func init() {
	runtime.RegisterFunction(failIfBadEntries)
	runtime.RegisterType(reflect.TypeOf((*diffFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*diffFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*elmCountCombineFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*elmCountCombineFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*errFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*errFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*failFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*failFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*failGBKFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*failGBKFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*failKVFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*failKVFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*hashFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*hashFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*nonEmptyFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*nonEmptyFn)(nil)).Elem())
	runtime.RegisterType(reflect.TypeOf((*sumFn)(nil)).Elem())
	schema.RegisterType(reflect.TypeOf((*sumFn)(nil)).Elem())
	reflectx.RegisterStructWrapper(reflect.TypeOf((*diffFn)(nil)).Elem(), wrapMakerDiffFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*elmCountCombineFn)(nil)).Elem(), wrapMakerElmCountCombineFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*errFn)(nil)).Elem(), wrapMakerErrFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*failFn)(nil)).Elem(), wrapMakerFailFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*failGBKFn)(nil)).Elem(), wrapMakerFailGBKFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*failKVFn)(nil)).Elem(), wrapMakerFailKVFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*hashFn)(nil)).Elem(), wrapMakerHashFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*nonEmptyFn)(nil)).Elem(), wrapMakerNonEmptyFn)
	reflectx.RegisterStructWrapper(reflect.TypeOf((*sumFn)(nil)).Elem(), wrapMakerSumFn)
	reflectx.RegisterFunc(reflect.TypeOf((*func(int, int) int)(nil)).Elem(), funcMakerIntInt??Int)
	reflectx.RegisterFunc(reflect.TypeOf((*func(int, func(*int) bool) error)(nil)).Elem(), funcMakerIntIterInt??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func(int, func(*string) bool) error)(nil)).Elem(), funcMakerIntIterString??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func(int, typex.T) int)(nil)).Elem(), funcMakerIntTypex??T??Int)
	reflectx.RegisterFunc(reflect.TypeOf((*func(int) error)(nil)).Elem(), funcMakerInt??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func(int) int)(nil)).Elem(), funcMakerInt??Int)
	reflectx.RegisterFunc(reflect.TypeOf((*func([]byte, func(*typex.T) bool, func(*typex.T) bool, func(t typex.T), func(t typex.T), func(t typex.T)) error)(nil)).Elem(), funcMakerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func([]byte, func(*typex.T) bool, func(*typex.T) bool, func(*typex.T) bool) error)(nil)).Elem(), funcMakerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func([]byte, func(*typex.Z) bool) error)(nil)).Elem(), funcMakerSliceOfByteIterTypex??Z??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func(typex.X, func(*typex.Y) bool) error)(nil)).Elem(), funcMakerTypex??XIterTypex??Y??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func(typex.X, typex.Y) error)(nil)).Elem(), funcMakerTypex??XTypex??Y??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func(typex.X) error)(nil)).Elem(), funcMakerTypex??X??Error)
	reflectx.RegisterFunc(reflect.TypeOf((*func() int)(nil)).Elem(), funcMaker??Int)
	exec.RegisterEmitter(reflect.TypeOf((*func(typex.T))(nil)).Elem(), emitMakerTypex??T)
	exec.RegisterInput(reflect.TypeOf((*func(*int) bool)(nil)).Elem(), iterMakerInt)
	exec.RegisterInput(reflect.TypeOf((*func(*string) bool)(nil)).Elem(), iterMakerString)
	exec.RegisterInput(reflect.TypeOf((*func(*typex.T) bool)(nil)).Elem(), iterMakerTypex??T)
	exec.RegisterInput(reflect.TypeOf((*func(*typex.Y) bool)(nil)).Elem(), iterMakerTypex??Y)
	exec.RegisterInput(reflect.TypeOf((*func(*typex.Z) bool)(nil)).Elem(), iterMakerTypex??Z)
}

func wrapMakerDiffFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*diffFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 []byte, a1 func(*typex.T) bool, a2 func(*typex.T) bool, a3 func(t typex.T), a4 func(t typex.T), a5 func(t typex.T)) error {
			return dfn.ProcessElement(a0, a1, a2, a3, a4, a5)
		}),
	}
}

func wrapMakerElmCountCombineFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*elmCountCombineFn)
	return map[string]reflectx.Func{
		"AddInput":          reflectx.MakeFunc(func(a0 int, a1 typex.T) int { return dfn.AddInput(a0, a1) }),
		"CreateAccumulator": reflectx.MakeFunc(func() int { return dfn.CreateAccumulator() }),
		"ExtractOutput":     reflectx.MakeFunc(func(a0 int) int { return dfn.ExtractOutput(a0) }),
		"MergeAccumulators": reflectx.MakeFunc(func(a0 int, a1 int) int { return dfn.MergeAccumulators(a0, a1) }),
	}
}

func wrapMakerErrFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*errFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 int) error { return dfn.ProcessElement(a0) }),
	}
}

func wrapMakerFailFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*failFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 typex.X) error { return dfn.ProcessElement(a0) }),
	}
}

func wrapMakerFailGBKFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*failGBKFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 typex.X, a1 func(*typex.Y) bool) error { return dfn.ProcessElement(a0, a1) }),
	}
}

func wrapMakerFailKVFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*failKVFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 typex.X, a1 typex.Y) error { return dfn.ProcessElement(a0, a1) }),
	}
}

func wrapMakerHashFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*hashFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 int, a1 func(*string) bool) error { return dfn.ProcessElement(a0, a1) }),
	}
}

func wrapMakerNonEmptyFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*nonEmptyFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 []byte, a1 func(*typex.Z) bool) error { return dfn.ProcessElement(a0, a1) }),
	}
}

func wrapMakerSumFn(fn any) map[string]reflectx.Func {
	dfn := fn.(*sumFn)
	return map[string]reflectx.Func{
		"ProcessElement": reflectx.MakeFunc(func(a0 int, a1 func(*int) bool) error { return dfn.ProcessElement(a0, a1) }),
	}
}

type callerIntInt??Int struct {
	fn func(int, int) int
}

func funcMakerIntInt??Int(fn any) reflectx.Func {
	f := fn.(func(int, int) int)
	return &callerIntInt??Int{fn: f}
}

func (c *callerIntInt??Int) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerIntInt??Int) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerIntInt??Int) Call(args []any) []any {
	out0 := c.fn(args[0].(int), args[1].(int))
	return []any{out0}
}

func (c *callerIntInt??Int) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.(int), arg1.(int))
}

type callerIntIterInt??Error struct {
	fn func(int, func(*int) bool) error
}

func funcMakerIntIterInt??Error(fn any) reflectx.Func {
	f := fn.(func(int, func(*int) bool) error)
	return &callerIntIterInt??Error{fn: f}
}

func (c *callerIntIterInt??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerIntIterInt??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerIntIterInt??Error) Call(args []any) []any {
	out0 := c.fn(args[0].(int), args[1].(func(*int) bool))
	return []any{out0}
}

func (c *callerIntIterInt??Error) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.(int), arg1.(func(*int) bool))
}

type callerIntIterString??Error struct {
	fn func(int, func(*string) bool) error
}

func funcMakerIntIterString??Error(fn any) reflectx.Func {
	f := fn.(func(int, func(*string) bool) error)
	return &callerIntIterString??Error{fn: f}
}

func (c *callerIntIterString??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerIntIterString??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerIntIterString??Error) Call(args []any) []any {
	out0 := c.fn(args[0].(int), args[1].(func(*string) bool))
	return []any{out0}
}

func (c *callerIntIterString??Error) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.(int), arg1.(func(*string) bool))
}

type callerIntTypex??T??Int struct {
	fn func(int, typex.T) int
}

func funcMakerIntTypex??T??Int(fn any) reflectx.Func {
	f := fn.(func(int, typex.T) int)
	return &callerIntTypex??T??Int{fn: f}
}

func (c *callerIntTypex??T??Int) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerIntTypex??T??Int) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerIntTypex??T??Int) Call(args []any) []any {
	out0 := c.fn(args[0].(int), args[1].(typex.T))
	return []any{out0}
}

func (c *callerIntTypex??T??Int) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.(int), arg1.(typex.T))
}

type callerInt??Error struct {
	fn func(int) error
}

func funcMakerInt??Error(fn any) reflectx.Func {
	f := fn.(func(int) error)
	return &callerInt??Error{fn: f}
}

func (c *callerInt??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerInt??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerInt??Error) Call(args []any) []any {
	out0 := c.fn(args[0].(int))
	return []any{out0}
}

func (c *callerInt??Error) Call1x1(arg0 any) any {
	return c.fn(arg0.(int))
}

type callerInt??Int struct {
	fn func(int) int
}

func funcMakerInt??Int(fn any) reflectx.Func {
	f := fn.(func(int) int)
	return &callerInt??Int{fn: f}
}

func (c *callerInt??Int) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerInt??Int) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerInt??Int) Call(args []any) []any {
	out0 := c.fn(args[0].(int))
	return []any{out0}
}

func (c *callerInt??Int) Call1x1(arg0 any) any {
	return c.fn(arg0.(int))
}

type callerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error struct {
	fn func([]byte, func(*typex.T) bool, func(*typex.T) bool, func(t typex.T), func(t typex.T), func(t typex.T)) error
}

func funcMakerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error(fn any) reflectx.Func {
	f := fn.(func([]byte, func(*typex.T) bool, func(*typex.T) bool, func(t typex.T), func(t typex.T), func(t typex.T)) error)
	return &callerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error{fn: f}
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error) Call(args []any) []any {
	out0 := c.fn(args[0].([]byte), args[1].(func(*typex.T) bool), args[2].(func(*typex.T) bool), args[3].(func(t typex.T)), args[4].(func(t typex.T)), args[5].(func(t typex.T)))
	return []any{out0}
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TEmitTypex??TEmitTypex??TEmitTypex??T??Error) Call6x1(arg0, arg1, arg2, arg3, arg4, arg5 any) any {
	return c.fn(arg0.([]byte), arg1.(func(*typex.T) bool), arg2.(func(*typex.T) bool), arg3.(func(t typex.T)), arg4.(func(t typex.T)), arg5.(func(t typex.T)))
}

type callerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error struct {
	fn func([]byte, func(*typex.T) bool, func(*typex.T) bool, func(*typex.T) bool) error
}

func funcMakerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error(fn any) reflectx.Func {
	f := fn.(func([]byte, func(*typex.T) bool, func(*typex.T) bool, func(*typex.T) bool) error)
	return &callerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error{fn: f}
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error) Call(args []any) []any {
	out0 := c.fn(args[0].([]byte), args[1].(func(*typex.T) bool), args[2].(func(*typex.T) bool), args[3].(func(*typex.T) bool))
	return []any{out0}
}

func (c *callerSliceOfByteIterTypex??TIterTypex??TIterTypex??T??Error) Call4x1(arg0, arg1, arg2, arg3 any) any {
	return c.fn(arg0.([]byte), arg1.(func(*typex.T) bool), arg2.(func(*typex.T) bool), arg3.(func(*typex.T) bool))
}

type callerSliceOfByteIterTypex??Z??Error struct {
	fn func([]byte, func(*typex.Z) bool) error
}

func funcMakerSliceOfByteIterTypex??Z??Error(fn any) reflectx.Func {
	f := fn.(func([]byte, func(*typex.Z) bool) error)
	return &callerSliceOfByteIterTypex??Z??Error{fn: f}
}

func (c *callerSliceOfByteIterTypex??Z??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerSliceOfByteIterTypex??Z??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerSliceOfByteIterTypex??Z??Error) Call(args []any) []any {
	out0 := c.fn(args[0].([]byte), args[1].(func(*typex.Z) bool))
	return []any{out0}
}

func (c *callerSliceOfByteIterTypex??Z??Error) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.([]byte), arg1.(func(*typex.Z) bool))
}

type callerTypex??XIterTypex??Y??Error struct {
	fn func(typex.X, func(*typex.Y) bool) error
}

func funcMakerTypex??XIterTypex??Y??Error(fn any) reflectx.Func {
	f := fn.(func(typex.X, func(*typex.Y) bool) error)
	return &callerTypex??XIterTypex??Y??Error{fn: f}
}

func (c *callerTypex??XIterTypex??Y??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerTypex??XIterTypex??Y??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerTypex??XIterTypex??Y??Error) Call(args []any) []any {
	out0 := c.fn(args[0].(typex.X), args[1].(func(*typex.Y) bool))
	return []any{out0}
}

func (c *callerTypex??XIterTypex??Y??Error) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.(typex.X), arg1.(func(*typex.Y) bool))
}

type callerTypex??XTypex??Y??Error struct {
	fn func(typex.X, typex.Y) error
}

func funcMakerTypex??XTypex??Y??Error(fn any) reflectx.Func {
	f := fn.(func(typex.X, typex.Y) error)
	return &callerTypex??XTypex??Y??Error{fn: f}
}

func (c *callerTypex??XTypex??Y??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerTypex??XTypex??Y??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerTypex??XTypex??Y??Error) Call(args []any) []any {
	out0 := c.fn(args[0].(typex.X), args[1].(typex.Y))
	return []any{out0}
}

func (c *callerTypex??XTypex??Y??Error) Call2x1(arg0, arg1 any) any {
	return c.fn(arg0.(typex.X), arg1.(typex.Y))
}

type callerTypex??X??Error struct {
	fn func(typex.X) error
}

func funcMakerTypex??X??Error(fn any) reflectx.Func {
	f := fn.(func(typex.X) error)
	return &callerTypex??X??Error{fn: f}
}

func (c *callerTypex??X??Error) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *callerTypex??X??Error) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *callerTypex??X??Error) Call(args []any) []any {
	out0 := c.fn(args[0].(typex.X))
	return []any{out0}
}

func (c *callerTypex??X??Error) Call1x1(arg0 any) any {
	return c.fn(arg0.(typex.X))
}

type caller??Int struct {
	fn func() int
}

func funcMaker??Int(fn any) reflectx.Func {
	f := fn.(func() int)
	return &caller??Int{fn: f}
}

func (c *caller??Int) Name() string {
	return reflectx.FunctionName(c.fn)
}

func (c *caller??Int) Type() reflect.Type {
	return reflect.TypeOf(c.fn)
}

func (c *caller??Int) Call(args []any) []any {
	out0 := c.fn()
	return []any{out0}
}

func (c *caller??Int) Call0x1() any {
	return c.fn()
}

type emitNative struct {
	n   exec.ElementProcessor
	fn  any
	est *sdf.WatermarkEstimator

	ctx   context.Context
	ws    []typex.Window
	et    typex.EventTime
	value exec.FullValue
}

func (e *emitNative) Init(ctx context.Context, ws []typex.Window, et typex.EventTime) error {
	e.ctx = ctx
	e.ws = ws
	e.et = et
	return nil
}

func (e *emitNative) Value() any {
	return e.fn
}

func (e *emitNative) AttachEstimator(est *sdf.WatermarkEstimator) {
	e.est = est
}

func emitMakerTypex??T(n exec.ElementProcessor) exec.ReusableEmitter {
	ret := &emitNative{n: n}
	ret.fn = ret.invokeTypex??T
	return ret
}

func (e *emitNative) invokeTypex??T(val typex.T) {
	e.value = exec.FullValue{Windows: e.ws, Timestamp: e.et, Elm: val}
	if e.est != nil {
		(*e.est).(sdf.TimestampObservingEstimator).ObserveTimestamp(e.et.ToTime())
	}
	if err := e.n.ProcessElement(e.ctx, &e.value); err != nil {
		panic(err)
	}
}

type iterNative struct {
	s  exec.ReStream
	fn any

	// cur is the "current" stream, if any.
	cur exec.Stream
}

func (v *iterNative) Init() error {
	cur, err := v.s.Open()
	if err != nil {
		return err
	}
	v.cur = cur
	return nil
}

func (v *iterNative) Value() any {
	return v.fn
}

func (v *iterNative) Reset() error {
	if err := v.cur.Close(); err != nil {
		return err
	}
	v.cur = nil
	return nil
}

func iterMakerInt(s exec.ReStream) exec.ReusableInput {
	ret := &iterNative{s: s}
	ret.fn = ret.readInt
	return ret
}

func (v *iterNative) readInt(value *int) bool {
	elm, err := v.cur.Read()
	if err != nil {
		if err == io.EOF {
			return false
		}
		panic(fmt.Sprintf("broken stream: %v", err))
	}
	*value = elm.Elm.(int)
	return true
}

func iterMakerString(s exec.ReStream) exec.ReusableInput {
	ret := &iterNative{s: s}
	ret.fn = ret.readString
	return ret
}

func (v *iterNative) readString(value *string) bool {
	elm, err := v.cur.Read()
	if err != nil {
		if err == io.EOF {
			return false
		}
		panic(fmt.Sprintf("broken stream: %v", err))
	}
	*value = elm.Elm.(string)
	return true
}

func iterMakerTypex??T(s exec.ReStream) exec.ReusableInput {
	ret := &iterNative{s: s}
	ret.fn = ret.readTypex??T
	return ret
}

func (v *iterNative) readTypex??T(value *typex.T) bool {
	elm, err := v.cur.Read()
	if err != nil {
		if err == io.EOF {
			return false
		}
		panic(fmt.Sprintf("broken stream: %v", err))
	}
	*value = elm.Elm.(typex.T)
	return true
}

func iterMakerTypex??Y(s exec.ReStream) exec.ReusableInput {
	ret := &iterNative{s: s}
	ret.fn = ret.readTypex??Y
	return ret
}

func (v *iterNative) readTypex??Y(value *typex.Y) bool {
	elm, err := v.cur.Read()
	if err != nil {
		if err == io.EOF {
			return false
		}
		panic(fmt.Sprintf("broken stream: %v", err))
	}
	*value = elm.Elm.(typex.Y)
	return true
}

func iterMakerTypex??Z(s exec.ReStream) exec.ReusableInput {
	ret := &iterNative{s: s}
	ret.fn = ret.readTypex??Z
	return ret
}

func (v *iterNative) readTypex??Z(value *typex.Z) bool {
	elm, err := v.cur.Read()
	if err != nil {
		if err == io.EOF {
			return false
		}
		panic(fmt.Sprintf("broken stream: %v", err))
	}
	*value = elm.Elm.(typex.Z)
	return true
}

// DO NOT MODIFY: GENERATED CODE

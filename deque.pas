program Deque;
type
    LongItem2Ptr = ^LongItem2;
    longItem2 = record
	data: longint;
	prev, next: LongItem2Ptr;
    end;
    LongDeque = record
	first, last: LongItem2Ptr;
    end;

procedure LongDequeInit(var deque: LongDeque);
begin
    deque.first := nil;
    deque.last := nil;
end;

procedure LongDequePushFront(var deque: LongDeque;var n: longint);
var
    tmp:LongItem2Ptr;
begin
    if deque.first = nil then
    begin
	new(deque.first);
	deque.first^.next := nil;
	deque.last := deque.first;
    end
    else
    begin
	new(deque.first^.prev);
	tmp := deque.first;
	deque.first := tmp^.prev;
	deque.first^.next := tmp;
    end;
    deque.first^.prev := nil;
    deque.first^.data := n;
end;

procedure LongDequePushBack(var deque: LongDeque;var n: longint);
var
    tmp: LongItem2Ptr;
begin
    if deque.last = nil then
    begin
	new(deque.last);
	deque.last^.prev := nil;
	deque.first := deque.last;
    end
    else
    begin
	new(deque.last^.next);
	tmp := deque.last;
	deque.last := tmp^.next;
	deque.last^.prev := tmp;
    end;
    deque.last^.data := n;
    deque.last^.next := nil;
end;

function LongDequePopFront(var deque: LongDeque; var n: longint) : boolean;
var
    tmp: LongItem2Ptr;
begin
    if deque.first = nil then
    begin
	LongDequePopFront := false;
	exit;
    end;
    n := deque.first^.data;
    tmp := deque.first^.next;
    dispose(deque.first);
    deque.first := tmp;
    LongDequePopFront := true;
end;

function LongDequePopBack(var deque: LongDeque; var n: longint) : boolean;
var
    tmp: LongItem2Ptr;
begin
    if deque.first = nil then
    begin
	LongDequePopBack := false;
	exit;
    end;
    n := deque.last^.data;
    tmp := deque.last^.prev;
    dispose(deque.last);
    deque.last := tmp;
    LongDequePopBack := true;
end;

function LongDequeIsEmpty(var deque: LongDeque) : boolean;
begin
    LongDequeIsEmpty := deque.first = nil;
end;
var
	d: LongDeque;
	n: longint;
begin
    LongDequeInit(d);
    while not SeekEof do
    begin
	readln(n);
	LongDequePushFront(d, n);
    end;
    while LongDequePopfront(d, n) do
    begin
	writeln(n);
    end;
end. 

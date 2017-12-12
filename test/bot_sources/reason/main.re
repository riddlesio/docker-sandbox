let issue_order = (s) => {
  Printf.printf("%s\n", s);
  flush(stdout);
};

let random_from_list = (lst) => {
  let len = List.length(lst);
  List.nth(lst, Random.int(len));
};

let split_char = (sep, str) => {
  let string_index_from = (i) =>
    try (Some(String.index_from(str, i, sep))) {
    | Not_found => None
    };
  let rec aux = (i, acc) =>
    switch (string_index_from(i)) {
    | Some(i') =>
      let w = String.sub(str, i, i' - i);
      aux(succ(i'), [w, ...acc]);
    | None =>
      let w = String.sub(str, i, String.length(str) - i);
      List.rev([w, ...acc]);
    };
  aux(0, []);
};

let process_line = (line) => {
  let tokens = split_char(' ', line);
  switch (List.nth(tokens, 0)) {
  | "action" =>
    let order = random_from_list(["paper", "scissors", "rock"]);
    issue_order(order);
  | _ => ()
  };
};

let read_lines =
  try (
    while (true) {
      let line = read_line();
      process_line(line);
    }
  ) {
  | End_of_file => ()
  };

try read_lines {
| exc => raise(exc)
};

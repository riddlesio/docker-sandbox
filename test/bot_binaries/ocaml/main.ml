let issue_order s =
   Printf.printf "%s\n" s;
   flush stdout;
;;

let random_from_list lst =
  let len = List.length lst in
    List.nth lst (Random.int len)
;;

let split_char sep str =
  let string_index_from i =
    try Some (String.index_from str i sep)
    with Not_found -> None
  in
  let rec aux i acc = match string_index_from i with
    | Some i' ->
        let w = String.sub str i (i' - i) in
        aux (succ i') (w::acc)
    | None ->
        let w = String.sub str i (String.length str - i) in
        List.rev (w::acc)
  in
  aux 0 []
;;

let process_line line =
  let tokens = split_char ' ' line in
  match (List.nth tokens 0) with
  | "action" ->
        let order = random_from_list ["paper"; "scissors"; "rock";] in
        issue_order order;
  | _ -> ()
;;

let read_lines =
  try
    while true do
      let line = read_line () in
        process_line line;
    done
  with End_of_file -> ()
;;

begin try
(
 read_lines
)
with exc ->
(
 raise exc
)
end;
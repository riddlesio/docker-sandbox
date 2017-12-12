//__main__

program RPS;

{$ifdef fpc}{$mode delphi}{$H+}{$endif}
{$ifndef fpc}{$apptype console}{$endif}

uses
  Classes, SysUtils;

procedure Run;
var
    s              : string;
    done           : Boolean;
    st             : TStringList;
    act            : string;
    MyRandomNumber : integer;
begin
    done := false;
    st:=TStringList.Create;
    try
        st.Delimiter:=#32; // space
        while not eof(input) do begin
            readln(s);

            if s = '' then Continue;
            st.DelimitedText:=s;
            if st.Count=0 then Continue;

            act := st[0];

            if act = 'action' then begin

                MyRandomNumber := random(3);
                if MyRandomNumber = 0 then writeln('rock')
                else if MyRandomNumber = 1 then writeln('paper')
                else if MyRandomNumber = 2 then writeln('scissors')

            end;
        if done then break;
        end;
    finally
        st.Free;
    end;
end;

begin
  run();
end.

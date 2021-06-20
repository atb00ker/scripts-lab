## Learn vscode

Here is a list of actions you can perform to increase your efficience with vscode:
My keybindings and shortcuts are different from default, you can find [my vscode configurations on GitHub](https://github.com/atb00ker/mconf/tree/master/files/vscode) and find your configurations at `~/.config/Code/User/`.

Now follow the steps below and complete the tutorial:

01. Open quickOpen menu[1] to search for `learn-file2.md`.
02. Open quickOpen menu[1] and convert it `command pallet` with the `>` followed by command. Type `> Install Extensions` to go to install extensions panel.
03. Open quickOpen menu[1] and convert it to `goto line` pallet with the `:` followed by line number. Type `:10` to come to this line.
04. Fold / Unfold: Go to `learn-file3.html`(step 01) and take your cursor to `div` with `class3` (step 03), now hit editor fold[2] & unfold[3] keys to quickly fold & unfold section.
05. Fold / Unfold all: Go to `learn-file3.html`(step 01) in command pallet(step 02) type `Fold All` and `Unfold All`.
06. Move by word: Go to `learn-file3.html`(step 01) and take your cursor to `div` with `class2`, now move inside the `div`, move faster with the help of word-by-word movements[4].`
07. Zen coding: Type `div.awesome+div#great` inside `div` with class two and press enter. Now enter `quick` in both the created HTML elements.
08. Quick find: Find `InputFocus` in this file with file finder[5] feature, type the string and press enter.
09. Word selection : Select the word `help` in this line with the help of word selection[6].
10. Line selection : Select this entire line[7] and copy it.
11. Block selection: Go to `learn-file4.py` (step 01) and find (step 08) function `IamFunctionOne`, now fold it (step 04) and use column select[8] to select the entire function.
12. Comment: Select `IamFunctionOne` in `learn-file4.py` (step 11), unfold it and comment it[9] out.
13. Select highlighted: You can select all highlighed instances of a word[10], select all the instances of `div` in this file.
14. Copy this line below[12].
15. Add another cursor below[13].
16. Add another cursor on next instance of of the word `step`[14].
17. Variable name: Go to `learn-file4.py` and change all the occurances of variable global `my_var`[15].
18. Search for the word `comment` in the entire workspace[16].
19. Go to extensions panel (step 02) and download coding snippets for Javascript named `xabikos.javascriptsnippets`, now create a new `.js` file and use any snippet from exntension's README.

Additional Exercises:
01. Select all instances of `step <stepnumber>` in this file using find (step 08) with regex and replace them all with format `step X<stepnumber>`. Now, selected all highlighed instances and copy all of them.
02. Create your own snippet.
03. Compare files: Select multiple files and find their diff from vscode.
04. Try [debugging in python](https://www.youtube.com/watch?v=w8QHoVam1-I)
05. Find shortcuts for moving to the start and end of the lines.

[1] : keybindings.json
```json
{
    "key": "alt+e",
    "command": "workbench.action.quickOpen"
}
```

[2] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+[",
    "command": "editor.fold",
    "when": "editorTextFocus && foldingEnabled"
}
```

[3] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+]",
    "command": "editor.unfold",
    "when": "editorTextFocus && foldingEnabled"
}
```

[4] : keybindings.json (Default)
```json
{
    "key": "ctrl+right",
    "command": "cursorWordEndRight",
    "when": "textInputFocus"
},
{
    "key": "ctrl+left",
    "command": "cursorWordEndLeft",
    "when": "textInputFocus"
}
```

[5] : keybindings.json (Default)
```json
{
    "key": "ctrl+f",
    "command": "actions.find",
    "when": "editorFocus || editorIsOpen"
}
```

[6] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+right",
    "command": "cursorWordEndRightSelect",
    "when": "textInputFocus"
},
{
    "key": "ctrl+shift+left",
    "command": "cursorWordEndLeftSelect",
    "when": "textInputFocus"
}
```

[7] : keybindings.json (Default)
```json
{
    "key": "ctrl+l",
    "command": "expandLineSelection",
    "when": "textInputFocus"
}
```

[8] : keybindings.json (Default)
```json
{
    "key": "shift+down",
    "command": "cursorColumnSelectDown",
    "when": "editorColumnSelection && textInputFocus"
}
```

[9] : keybindings.json (Default)
```json
{
    "key": "ctrl+/",
    "command": "editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
}
```

[10] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+l",
    "command": "editor.action.selectHighlights",
    "when": "editorFocus"
}
```

[11] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+l",
    "command": "editor.action.selectHighlights",
    "when": "editorFocus"
}
```

[12] : keybindings.json
```json
{
    "key": "ctrl+shift+d",
    "command": "editor.action.copyLinesDownAction",
    "when": "editorTextFocus && !editorReadonly"
}
```

[13] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+down",
    "command": "editor.action.insertCursorBelow",
    "when": "editorTextFocus"
}
```

[14] : keybindings.json (Default)
```json
{
    "key": "ctrl+d",
    "command": "editor.action.addSelectionToNextFindMatch",
    "when": "editorFocus"
}
```

[15] : keybindings.json (Default)
```json
{
    "key": "f2",
    "command": "editor.action.rename",
    "when": "editorHasRenameProvider && editorTextFocus && !editorReadonly"
}
```

[16] : keybindings.json (Default)
```json
{
    "key": "ctrl+shift+f",
    "command": "workbench.action.findInFiles"
}
```

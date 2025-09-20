# Game Engine Commands

This reference summarizes various game engine and quest commands available in X3TC scripting.

- `abort god event`: Ends a god event before its normal completion.
- `add encyclopedia custom article`: Creates a new encyclopedia entry (History, Information, News, or Stories).
- `<RefObj> add event listener`: Attaches a script to an object that runs when a specified event occurs.
- `al engine: register script=<Script Name>`: Registers a script with the Artificial Life (AL) engine.
- `al engine: set plugin <Var/String> description to <Var/String>`: Updates the description text shown for a registered AL plugin.
- `al engine: set plugin <Var/String> timer interval to <Var/Number> s`: Sets how often an AL plugin runs.
- `al engine: unregister script <Script Name>`: Removes a script from AL engine management.
- `change event news availability`: Controls news article availability based on race, sector, and jump range.
- `<RetVar/IF> display news article`: Shows a news article with optional placeholders and display limits.
- `finish god event`: Marks a god event as completed and triggers post-event logic.
- #### Rule: `<RetVar/IF> get global variable: name=<Var/String>`
- **Full Description:** Retrieves the value of a named global variable.
- **Examples:**
  - `$al.Settings = get global variable: name='al.LI.FDN.event'`
  - `$config.Array = get global variable: name='config.scripts'`
- **Edge Cases:** _None._
- `register god event: script=<Script Name> mask=<Var/Number>`: Registers a script to run as a god event with a condition mask.
- `register quest script <Script Name> instance multiple=<Var/Number>`: Registers a quest script, allowing multiple instances when needed.
- `remove encyclopedia custom article: id=<Var/String>`: Deletes a custom encyclopedia entry.
- `<RefObj> remove event listener: quest/event=<Var/Quest>`: Detaches an event listener script from an object.
- `<RetVar> script engine version`: Returns the script engine's version number.
- `set encyclopedia custom article sectors: id=<Var/String>, sector array=<Var/Array>`: Restricts a custom article to specified sectors.
- #### Rule: `set global variable: name=<Var/String> value=<Value>`
- **Full Description:** Sets or creates a global variable.
- **Examples:**
  - `set global variable: name=$var value=null`
  - `set global variable: name='al.LI.FDN.event' value=$al.Settings`
- **Edge Cases:** _None._
- `set quest/event <Var/Quest> alive=<Var/Number>`: Enables or disables a quest/event.
- `set quest/event <Var/Quest> timer to <Var/Number>`: Sets a countdown before a quest/event triggers or expires.
- `set quest/event <Var/Quest> timeout to <Var/Number>`: Defines how long a quest/event remains active before auto-completion or failure.
- `set quest/event <Var/Quest> state=<Var/Number> msg=<Var/String>`: Updates the internal state of a quest/event and optionally sends a message.

Postmortum - Adventurer Journey Solution

Language Choice – Python
I chose Python for its speed of iteration and readability. The challenge emphasized clarity of logic rather than raw performance, and Python’s syntax makes it easy to express parsing, coordinate updates, and CLI handling concisely. It also comes with strong standard library support meaning no dependencies required (unless you want to run the test suite).

Dual Movement Models
The story describes the hero as “facing North”, which to me, coming from a game development background, screams orientation-based movement. Plus the instructions would be better suited to include the cardinal directions (12N9E) if the fixed-axes model is preferred. Rather than guess which interpretation is preferred, I implemented both. The default "turn-then-move” model mirrors typical character control: `L`/`R` rotate 90°, `B` rotates 180°, and the adventurer walks forward. The alternative `--fixed-axes` mode treats the letters as absolute displacements.  Implementing both models lets me verify my assumption while still giving the second answer if the spec were to be interpreted differently.

Data Choices - Storing All Coordinates
Even though the final distance only depends on the start and end points, I opted to store every coordinate along the way. Again, coming from a game development background, I instinctively model movement as a path rather than a single offset. It makes debugging, visualizing, and optionally adding features (like a plotted path or animation) trivial, without adding complexity. If path lengths were egregiously long, I would reconsider storing all coordinates.

Validation - Zero-step Tokens
Initially I rejected instructions with zero steps. During testing I realized a `0L` token in the turn-then-move model is effectively a pure rotation command, which is actually useful for scripting headings. I relaxed the validation accordingly. The parser now accepts zero-step tokens and the movement loop handles them naturally.

Future Extensions
If expanded, this could visualize the path, output JSON for testing, or report both model results side-by-side. The architecture already supports that with minimal change.
from django.core.management.base import BaseCommand

from quiz.models import Language, Question


def q(text, a, b, c, d, correct):
    return {"text": text, "a": a, "b": b, "c": c, "d": d, "correct": correct}


LOW_PY = [
    q("What is a correct file extension for Python?", ".py", ".pt", ".pn", ".python", "a"),
    q("Which keyword defines a function in Python?", "def", "function", "fn", "define", "a"),
    q("How do you print to the console in Python 3?", "print()", "echo()", "println()", "console.log()", "a"),
    q("Which type represents whole numbers in Python?", "int", "float", "str", "bool", "a"),
    q("What symbol starts a comment in Python?", "#", "//", "/*", "--", "a"),
    q("Which of these is a Python list literal?", "[1, 2]", "{1, 2}", "(1, 2)", "<1, 2>", "a"),
    q("How do you create a string in Python?", "Quotes", "Semicolons", "Brackets only", "Dollar sign", "a"),
    q("What does `len([1,2,3])` return?", "3", "2", "4", "6", "a"),
    q("Which operator checks equality in Python?", "==", "=", "===", "eq", "a"),
    q("What is the output of `bool([])` in Python?", "False", "True", "Error", "None", "a"),
    q("Which keyword imports a module?", "import", "include", "use", "require", "a"),
    q("What is None in Python?", "Absence of value", "Zero", "Empty string", "False only", "a"),
]

MED_PY = [
    q("What is a list comprehension?", "Compact loop to build a list", "A type of comment", "GUI widget", "Import alias", "a"),
    q("What does `*args` typically collect?", "Positional arguments", "Keyword only", "Return values", "Exceptions", "a"),
    q("What is a decorator?", "Function that wraps another function", "A CSS class", "A database table", "A test runner", "a"),
    q("Which is immutable in Python?", "tuple", "list", "dict", "set", "a"),
    q("What does `with open(...) as f` ensure?", "File is closed properly", "Faster disk", "Unicode only", "Binary mode", "a"),
    q("What is a generator?", "Iterator from yield", "Random number", "Compiler pass", "Package installer", "a"),
    q("What is GIL often associated with?", "Threading in CPython", "Graphics", "Garbage size", "Global imports", "a"),
    q("Which creates a virtual environment (common tool)?", "venv", "npm", "gradle", "cargo", "a"),
    q("What does `self` refer to in instance methods?", "The instance", "The class", "The module", "The interpreter", "a"),
    q("What is `__init__`?", "Constructor hook", "Destructor", "Import hook", "String format", "a"),
    q("Which module is in the standard library for JSON?", "json", "simplejson", "ujson", "pickle", "a"),
    q("What is a dict key requirement (typical)?", "Hashable", "Always str", "Always int", "Must be list", "a"),
]

HIGH_PY = [
    q("What does `@staticmethod` imply?", "No implicit first argument", "Receives self", "Receives cls", "Async only", "a"),
    q("What is a descriptor protocol method?", "__get__", "__iter__", "__next__", "__all__", "a"),
    q("What is asyncio primarily for?", "Concurrent I/O", "Faster CPU math", "Memory compaction", "Syntax sugar", "a"),
    q("What does `functools.lru_cache` do?", "Memoizes a function", "Sorts lists", "Parses JSON", "Hashes passwords", "a"),
    q("What is a metaclass?", "Class of a class", "Imported alias", "Inline function", "Type hint only", "a"),
    q("What does `collections.deque` optimize?", "Append/pop ends", "Sorting", "Set union", "Regex", "a"),
    q("What is the MRO?", "Method resolution order", "Module read only", "Memory recover order", "Meta regex object", "a"),
    q("What does `typing.Protocol` enable?", "Structural subtyping", "Faster dicts", "DB migrations", "Async sleep", "a"),
    q("What is a context manager protocol?", "__enter__ / __exit__", "__init__ / __del__", "try / except", "import / from", "a"),
    q("Which is true of `multiprocessing` vs `threading` for CPU-bound?", "Separate processes help", "Threads always faster", "Same GIL benefits", "No difference", "a"),
    q("What is `__slots__` used for?", "Restrict instance attributes", "Add mixins", "Define operators", "Enable async", "a"),
    q("What does `itertools.groupby` require?", "Sorted iterable by key", "Random iterable", "Only strings", "Only numbers", "a"),
]

LOW_JAVA = [
    q("Which keyword declares a class in Java?", "class", "struct", "object", "type", "a"),
    q("What is the entry point method signature?", "public static void main(String[] args)", "void main()", "start()", "run()", "a"),
    q("Which is a primitive type in Java?", "int", "String", "Integer", "Object", "a"),
    q("How do you declare a constant with Java convention?", "static final", "const", "define", "val", "a"),
    q("Which access modifier is most restrictive?", "private", "protected", "public", "package", "a"),
    q("What does JVM stand for?", "Java Virtual Machine", "Java Visual Model", "Joint Variable Map", "Just Virtual Module", "a"),
    q("Which creates a new object in Java?", "new", "malloc", "alloc", "create", "a"),
    q("What ends every statement in Java?", "Semicolon", "Newline only", "Comma", "Period", "a"),
    q("Which package is implicit?", "java.lang", "java.util", "java.io", "java.net", "a"),
    q("What is inheritance keyword?", "extends", "inherits", "derive", "superclass", "a"),
    q("Which loop checks condition before each iteration?", "while", "do-while first", "for-each only", "repeat-until", "a"),
    q("What is `==` for objects by default?", "Reference equality", "Value equality", "Compile error", "Always true", "a"),
]

MED_JAVA = [
    q("What is an interface in Java?", "Contract without concrete implementation", "A GUI panel", "A database", "A thread", "a"),
    q("What does `final` on a variable mean?", "Cannot reassign", "Must be static", "Must be public", "Optional", "a"),
    q("What is method overloading?", "Same name, different parameters", "Same name, same params", "Override parent", "Rename method", "a"),
    q("What is method overriding?", "Subclass replaces parent implementation", "Duplicate in same class", "Private method", "Static only", "a"),
    q("What is `try/catch` for?", "Exception handling", "Loops", "Imports", "Generics", "a"),
    q("What is a checked exception?", "Must be declared or caught", "Always runtime", "Never thrown", "Optional compile", "a"),
    q("What does `ArrayList` use internally?", "Dynamic array", "Linked list", "Hash table", "Tree", "a"),
    q("What is autoboxing?", "Primitive to wrapper conversion", "Garbage collection", "String interning", "Lambda capture", "a"),
    q("What is `this`?", "Current instance reference", "Parent class", "Static context", "Module path", "a"),
    q("What is `super`?", "Parent class reference", "Child class", "Static import", "Package root", "a"),
    q("Which collection stores unique elements?", "Set", "List", "Queue", "Deque", "a"),
    q("What is a package?", "Namespace for classes", "Compiled jar", "Build tool", "Thread pool", "a"),
]

HIGH_JAVA = [
    q("What is erasure in Java generics?", "Type params removed at runtime", "Faster boxing", "Stronger typing at runtime", "Reflection boost", "a"),
    q("What does `volatile` hint to?", "Visibility across threads", "Immutable object", "Heap offloading", "Native code", "a"),
    q("What is a functional interface?", "Single abstract method", "No methods", "Only static methods", "Annotation only", "a"),
    q("What is `synchronized` used for?", "Mutual exclusion", "Faster IO", "Immutable strings", "Serialization", "a"),
    q("What is the Streams API primarily for?", "Declarative data processing", "Socket streams only", "File bytes only", "GUI events", "a"),
    q("What is `Optional` intended to express?", "Explicit maybe-absent value", "Required field", "Thread option", "GC hint", "a"),
    q("What is reflection?", "Inspect/modify types at runtime", "Shader compilation", "Regex engine", "JIT phase", "a"),
    q("What does `transient` mean on a field?", "Skipped in default serialization", "Always serialized", "Final", "Volatile", "a"),
    q("What is a module in Java 9+?", "Strong encapsulation unit", "Maven only", "Gradle only", "OS process", "a"),
    q("What is `CompletableFuture` for?", "Async composition", "Low-level sockets", "Swing layout", "JDBC driver", "a"),
    q("What is the difference between `Comparable` and `Comparator`?", "Natural vs external order", "Same thing", "Only primitives", "Threading", "a"),
    q("What is a memory leak risk with listeners?", "Strong references prevent GC", "Weak refs always leak", "Primitives leak", "final fields", "a"),
]

LOW_JS = [
    q("Which tag embeds JavaScript in HTML?", "<script>", "<js>", "<javascript>", "<code>", "a"),
    q("How do you declare a variable with block scope (ES6)?", "let", "var", "global", "def", "a"),
    q("What is `typeof null` in JavaScript?", "object", "null", "undefined", "boolean", "a"),
    q("Which method selects one DOM element by CSS selector?", "querySelector", "getId", "findOne", "select", "a"),
    q("What does `===` compare?", "Value and type", "Value only", "Reference only", "Nothing", "a"),
    q("Which creates a function expression?", "const f = () => {}", "function()", "lambda def", "fn f()", "a"),
    q("What is JSON?", "Text data format", "A database", "A JS engine", "A CSS preprocessor", "a"),
    q("Which is falsy in JavaScript?", "0", "[]", "{}", "new Date()", "a"),
    q("How do you add an event listener in the DOM API?", "addEventListener", "on()", "listen()", "bind()", "a"),
    q("What does `Array.prototype.map` return?", "New array", "Same array mutated", "Single value", "Boolean", "a"),
    q("What is `NaN`?", "Not a Number", "Null and None", "New a Node", "Native API Name", "a"),
    q("Which keyword declares a constant binding?", "const", "let", "var", "static", "a"),
]

MED_JS = [
    q("What is a closure?", "Function + lexical environment", "Anonymous class", "TCP socket", "CSS rule", "a"),
    q("What is the event loop?", "Schedules async callbacks", "Graphics loop", "Game loop only", "Parser pass", "a"),
    q("What is hoisting (var)?", "Declaration moved conceptually", "Values moved", "Imports removed", "Strict error", "a"),
    q("What does `Promise` represent?", "Future async result", "DOM node", "Regex match", "Map key", "a"),
    q("What is `async/await` built on?", "Promises", "Callbacks only", "Threads", "Generators only", "a"),
    q("What is destructuring?", "Unpack properties/elements", "Minifying code", "Tree shaking", "Bundling", "a"),
    q("What is the spread operator `...` used for?", "Expanding iterables", "Rest only in params", "Comments", "Types", "a"),
    q("What is `this` in a normal function call?", "Depends on call site", "Always window", "Always undefined", "Lexical only", "a"),
    q("What is a module in ES modules?", "File with import/export", "npm package only", "React component", "Worker", "a"),
    q("What does `fetch` return?", "Promise", "XMLHttpRequest", "string", "Buffer", "a"),
    q("What is strict mode?", "Opt-in stricter semantics", "Faster mode", "Minified mode", "TypeScript", "a"),
    q("What is `localStorage`?", "Key-value web storage", "Server database", "Cookie only", "Indexed table", "a"),
]

HIGH_JS = [
    q("What is a microtask queue related to?", "Promise callbacks (among others)", "setTimeout only", "Rendering only", "Parsing", "a"),
    q("What is prototypal inheritance?", "Objects delegate to prototypes", "Class-only inheritance", "Copy-based", "Interface-based", "a"),
    q("What does `WeakMap` key requirement?", "Objects (weakly held)", "Strings only", "Numbers only", "Symbols only", "a"),
    q("What is a Symbol used for?", "Unique property keys", "Math constants", "Regex flags", "Async ids", "a"),
    q("What is tree shaking?", "Dead code elimination", "DOM traversal", "BST sort", "CSS layout", "a"),
    q("What is `Proxy`?", "Intercept object operations", "HTTP client", "Service worker", "WebSocket", "a"),
    q("What is `BigInt` for?", "Arbitrary-precision integers", "Floats", "Decimals currency", "UUID", "a"),
    q("What is TDZ?", "Temporal dead zone (let/const)", "Time zone DB", "Task delay zone", "Thread dump zone", "a"),
    q("What is `import()`?", "Dynamic import", "Static only", "CSS import", "SQL import", "a"),
    q("What is `SharedArrayBuffer` sensitive to?", "Spectre-like concerns / COOP/COEP", "CSS", "Fonts", "SVG", "a"),
    q("What is `structuredClone`?", "Deep clone structured data", "Shallow assign", "JSON.parse only", "Immutable freeze", "a"),
    q("What is `Atomics` for?", "Shared memory coordination", "CSS units", "Crypto hashing", "Regex atoms", "a"),
]

LOW_SQL = [
    q("Which statement retrieves rows?", "SELECT", "GET", "FETCH", "READ", "a"),
    q("Which clause filters rows?", "WHERE", "FILTER", "HAVING only", "IF", "a"),
    q("Which keyword removes duplicate rows from results?", "DISTINCT", "UNIQUE", "DEDUP", "ONLY", "a"),
    q("Which statement adds new rows?", "INSERT", "ADD", "CREATE ROW", "APPEND", "a"),
    q("Which statement changes existing rows?", "UPDATE", "MODIFY", "SET ROW", "ALTER ROW", "a"),
    q("Which statement removes rows?", "DELETE", "REMOVE", "DROP ROW", "TRUNCATE ROW", "a"),
    q("What does `COUNT(*)` do?", "Counts rows", "Sums column", "Averages", "Joins", "a"),
    q("Which join returns matching rows from both tables?", "INNER", "LEFT", "RIGHT", "FULL outer always", "a"),
    q("Which keyword sorts results?", "ORDER BY", "SORT", "ARRANGE", "GROUP", "a"),
    q("What is a primary key?", "Unique row identifier", "Foreign reference", "Index only", "View", "a"),
    q("Which creates a table?", "CREATE TABLE", "NEW TABLE", "MAKE TABLE", "ADD TABLE", "a"),
    q("What does `NULL` represent?", "Unknown / missing", "Zero", "Empty string", "False", "a"),
]

MED_SQL = [
    q("What does `GROUP BY` do?", "Aggregates per group", "Sorts only", "Filters rows", "Joins tables", "a"),
    q("When is `HAVING` used?", "Filter aggregated results", "Filter before group", "Sort", "Limit", "a"),
    q("What is a foreign key?", "References another table key", "Primary only", "Unique index", "Check constraint", "a"),
    q("What is a transaction?", "Atomic unit of work", "A table", "A view", "A trigger only", "a"),
    q("What does `JOIN ... ON` specify?", "Join condition", "Sort key", "Index name", "Alias only", "a"),
    q("What is normalization?", "Reduce redundancy", "Add duplicates", "Encrypt columns", "Shard data", "a"),
    q("What is an index for?", "Faster lookups (typically)", "Slower writes always", "Encryption", "Backup", "a"),
    q("What does `LIKE` do?", "Pattern match strings", "Numeric compare", "Date diff", "Cast types", "a"),
    q("What is a subquery?", "Query inside another", "Parallel server", "Stored file", "Index type", "a"),
    q("What is `UNION`?", "Combine result sets", "Join columns", "Transaction", "Grant", "a"),
    q("What does `CASE` provide?", "Conditional expressions", "Switch database", "Error handling", "Locking", "a"),
    q("What is a view?", "Stored query (virtual table)", "Physical table", "Index", "User", "a"),
]

HIGH_SQL = [
    q("What isolation level may allow phantom reads?", "READ COMMITTED (depends on DB)", "SERIALIZABLE", "None", "SNAPSHOT never", "a"),
    q("What is a deadlock?", "Circular lock wait", "Missing index", "Corrupt page", "Slow disk", "a"),
    q("What does `EXPLAIN` help with?", "Query plan analysis", "Grant permissions", "Backup", "Replication", "a"),
    q("What is a covering index?", "Index includes queried columns", "Full table scan", "Hash only", "Temp table", "a"),
    q("What is MVCC broadly?", "Multi-version concurrency", "Multi-view cache", "Multi-vendor connect", "Manual vacuum", "a"),
    q("What is a window function?", "Computes over row partitions", "GUI widget", "Session var", "Trigger", "a"),
    q("What is CTE?", "WITH clause named subquery", "Commit", "Constraint", "Charset", "a"),
    q("What is a recursive CTE used for?", "Hierarchical/graph traversals", "Speeding inserts", "Encryption", "Sharding", "a"),
    q("What does `UPSERT` pattern mean?", "Insert or update", "Delete all", "Read only", "Grant", "a"),
    q("What is a materialized view?", "Stored snapshot of query", "Normal view", "Temp table only", "Index", "a"),
    q("What is star schema?", "Fact + dimension tables", "No keys", "Graph only", "Key-value", "a"),
    q("What is write skew?", "Anomaly with row-level locks", "Disk skew", "Join order", "Index imbalance", "a"),
]

LOW_REACT = [
    q("What is React primarily used for?", "Building UIs", "Databases", "OS kernels", "Game engines", "a"),
    q("What syntax mixes JS and markup in React?", "JSX", "HTMLX", "RXML", "TSX only", "a"),
    q("What returns UI from a function component?", "return JSX", "render()", "paint()", "draw()", "a"),
    q("Which hook stores component state?", "useState", "useStore", "useVar", "useMemo only", "a"),
    q("Which hook handles side effects?", "useEffect", "useSide", "useAsync", "useDOM", "a"),
    q("How do you pass data to a child?", "props", "globals", "imports", "window", "a"),
    q("What is a key prop used for?", "List reconciliation", "Security", "Styling", "Routing", "a"),
    q("What triggers a re-render (typically)?", "State/props change", "Timer only", "CSS change", "DOM id", "a"),
    q("What is the virtual DOM idea?", "Lightweight tree diffing", "Browser DOM copy", "Canvas only", "WebGL", "a"),
    q("Which tool commonly bootstraps React apps?", "Vite / CRA", "Maven", "Gradle", "pip", "a"),
    q("What is a component?", "Reusable UI piece", "A database table", "A CSS file", "A server", "a"),
    q("What does `npm start` often do?", "Run dev server", "Deploy prod", "Run tests only", "Lint only", "a"),
]

MED_REACT = [
    q("What is `useMemo` for?", "Memoize computed values", "Store state", "Fetch data", "Subscribe events", "a"),
    q("What is `useCallback` for?", "Stable function identity", "Memoize objects", "Debounce network", "CSS memo", "a"),
    q("What is lifting state up?", "Move state to common ancestor", "Delete state", "Use context only", "Redux only", "a"),
    q("What is controlled input?", "Value driven by React state", "Unmanaged DOM", "File only", "Canvas", "a"),
    q("What does `useRef` hold?", "Mutable box across renders", "Derived state", "Async cache", "Router", "a"),
    q("What is React Router for?", "Client-side routing", "Server routing only", "State management", "Styling", "a"),
    q("What is context used for?", "Avoid prop drilling", "Replace hooks", "Replace JSX", "SSR only", "a"),
    q("What is `useReducer` suited for?", "Complex state transitions", "Simple counter only", "Animations only", "HTTP", "a"),
    q("What are fragments?", "Group without extra DOM", "Shadow DOM", "Portals", "Suspense", "a"),
    q("What is Strict Mode (dev)?", "Extra checks/warnings", "Production optimizer", "Router mode", "CSS mode", "a"),
    q("What is code splitting often done with?", "dynamic import()", "inline styles", "useMemo", "useRef", "a"),
    q("What is `key` in lists mainly for?", "Identity stability", "CSS class", "Accessibility", "SEO", "a"),
]

HIGH_REACT = [
    q("What is concurrent rendering about?", "Interruptible work scheduling", "Faster CPU", "Web Workers", "SSR only", "a"),
    q("What is `useLayoutEffect` timing?", "After DOM mutations, before paint", "After paint", "Before commit", "Idle only", "a"),
    q("What is `Suspense` used with?", "Async boundaries (e.g. lazy)", "Only errors", "Only forms", "Only CSS", "a"),
    q("What is `ErrorBoundary`?", "Catch render errors in subtree", "Catch fetch errors always", "Router guard", "Lint rule", "a"),
    q("What does `flushSync` do?", "Force synchronous flush", "Debounce updates", "Batch forever", "Cancel render", "a"),
    q("What is hydration?", "Attach React to SSR HTML", "Drink water", "Cache warming", "Prefetch", "a"),
    q("What is `useDeferredValue` for?", "Defer updating expensive UI", "Debounce input", "Throttle scroll", "Memoize", "a"),
    q("What is `useTransition` for?", "Mark updates non-urgent", "Route changes only", "Animations only", "HTTP", "a"),
    q("What is `React.memo`?", "Shallow prop compare wrapper", "Deep compare", "Context provider", "Reducer", "a"),
    q("What is a portal?", "Render outside parent DOM hierarchy", "WebSocket", "Worker", "Iframe", "a"),
    q("What is reconciliation?", "Diffing algorithm", "Network retry", "CSS layout", "Bundle split", "a"),
    q("Why avoid index as key (often)?", "Reorders break identity", "SEO", "Security", "Performance always better", "a"),
]


class Command(BaseCommand):
    help = "Seed languages and questions for Skill up demo."

    def handle(self, *args, **options):
        Language.objects.all().delete()
        Question.objects.all().delete()

        specs = [
            ("Python", "python", "fa-brands fa-python", "Popular for APIs, data, and automation.", 1, LOW_PY, MED_PY, HIGH_PY),
            ("Java", "java", "fa-brands fa-java", "Enterprise apps and Android ecosystem.", 2, LOW_JAVA, MED_JAVA, HIGH_JAVA),
            (
                "JavaScript",
                "javascript",
                "fa-brands fa-js",
                "The language of the web.",
                3,
                LOW_JS,
                MED_JS,
                HIGH_JS,
            ),
            ("SQL", "sql", "fa-solid fa-database", "Query and model relational data.", 4, LOW_SQL, MED_SQL, HIGH_SQL),
            ("React", "react", "fa-brands fa-react", "Component-driven UI engineering.", 5, LOW_REACT, MED_REACT, HIGH_REACT),
        ]

        total = 0
        for name, slug, icon, blurb, order, low, med, high in specs:
            lang = Language.objects.create(
                name=name, slug=slug, icon_class=icon, blurb=blurb, order=order
            )
            buckets = [
                (Question.Difficulty.LOW, low),
                (Question.Difficulty.MED, med),
                (Question.Difficulty.HIGH, high),
            ]
            for diff, items in buckets:
                for item in items:
                    Question.objects.create(
                        language=lang,
                        difficulty=diff,
                        text=item["text"],
                        choice_a=item["a"],
                        choice_b=item["b"],
                        choice_c=item["c"],
                        choice_d=item["d"],
                        correct=item["correct"],
                    )
                    total += 1

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(specs)} languages and {total} questions."))

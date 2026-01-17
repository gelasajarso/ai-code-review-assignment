# Notes

- Email validation in Task 2 intentionally uses a minimal structural heuristic rather than full RFC 5322 compliance to avoid overengineering and external dependencies. The goal was to improve correctness and safety relative to the original implementation while keeping the logic reviewable and maintainable.

- For Tasks 1 and 3, a return value of `0.0` is used when no valid items are present. This choice avoids raising exceptions and provides a predictable, safe default behavior consistent with many production analytics contexts.

- Input schemas were assumed to be loosely structured collections based on the original implementations. The fixes focus on correcting core logical and safety issues without enforcing strict schema validation beyond what is necessary.

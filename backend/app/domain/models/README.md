# Domain Models Layer (The Core)

Este directorio contiene las **Entidades de Dominio** del proyecto hBnb.

### Principios de esta capa:
1. **Independencia Total:** Estos modelos son Python puro (`dataclasses`). No dependen de frameworks (FastAPI), ni de ORMs (SQLAlchemy), ni de librerías de validación (Pydantic).
2. **Lógica de Negocio:** Aquí reside la verdad del negocio. Cualquier regla que defina qué es un `User` o un `Place` debe nacer aquí.
3. **DRY (Don't Repeat Yourself):** Se utiliza un `BaseModel` para centralizar atributos comunes (`id`, `created_at`, `updated_at`).

### Estructura de Archivos:
- `base_model.py`: Clase base con lógica de timestamps y UUIDs.
- `user.py`, `place.py`, `review.py`: Entidades desacopladas para facilitar el mantenimiento y evitar imports circulares.

### Nota sobre Imports:
Para mantener la coherencia en los imports internos, se utilizan **imports relativos** (ej. `from .base_model import BaseModel`). Para uso externo, se recomienda importar desde el paquete raíz del dominio:
`from app.domain.models import User`
#!/usr/bin/env bash
# Prepara graphify al iniciar sesión: lo instala si falta y reconstruye el grafo de código.
# Nunca bloquea el inicio: cualquier fallo se ignora.
set -u
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0
if ! command -v graphify >/dev/null 2>&1; then
  pip install -q graphifyy==0.9.108 >/dev/null 2>&1 || pip install -q --user graphifyy==0.9.108 >/dev/null 2>&1 || exit 0
fi
timeout 120 graphify update . >/dev/null 2>&1 || true
[ -f graphify-out/graph.json ] && echo "graphify listo: usa 'graphify query \"<pregunta>\"' antes de grep/read."
exit 0

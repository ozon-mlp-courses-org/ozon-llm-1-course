# Семинар по теме "Prompt Engineering"

Установка зависимостей

```bash
uv sync
```

Сервер, в отдельном терминале можно запустить так:

```bash
export VLLM_CPU_KVCACHE_SPACE=4
export VLLM_USE_V2_MODEL_RUNNER=0
uv run vllm serve RedHatAI/Qwen3.5-4B-quantized.w8a8 \
    --language-model-only \
    --max-model-len 8192 \
    --reasoning-parser qwen3 \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --generation-config vllm \
    --max-logprobs -1 \
    --no-enable-chunked-prefill \
    --max-num-batched-tokens 8192 \
    --no-enable-prefix-caching \
    --structured-outputs-config '{"backend": "xgrammar", "disable_any_whitespace": true}' \
    --port 8000
```

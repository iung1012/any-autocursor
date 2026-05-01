export const TASK_STATUS_VARIANTS: Record<string, any> = {
  pending: 'secondary',
  claimed: 'secondary',
  running: 'default',
  succeeded: 'success',
  failed: 'danger',
  interrupted: 'warning',
  cancel_requested: 'warning',
  cancelled: 'warning',
}

export const TERMINAL_TASK_STATUSES = new Set([
  'succeeded',
  'failed',
  'interrupted',
  'cancelled',
])

export function isTerminalTaskStatus(status: string) {
  return TERMINAL_TASK_STATUSES.has(status)
}

export function getTaskStatusText(status: string) {
  switch (status) {
    case 'succeeded':
      return 'Concluído'
    case 'failed':
      return 'Falhou'
    case 'interrupted':
      return 'Interrompido'
    case 'cancelled':
      return 'Cancelado'
    case 'cancel_requested':
      return 'Cancelando'
    case 'running':
      return 'Executando'
    case 'claimed':
      return 'Recebido'
    case 'pending':
      return 'Na fila'
    default:
      return status
  }
}

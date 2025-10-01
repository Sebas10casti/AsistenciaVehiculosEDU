import { VEHICLE_TYPE_LABELS, AREA_LABELS } from '../constants/app.constants';

/**
 * Utilidades para el sistema de control de acceso vehicular
 */
export class AppUtils {

  /**
   * Obtener el label de un tipo de vehículo
   */
  static getVehicleTypeLabel(tipo: string): string {
    return VEHICLE_TYPE_LABELS[tipo as keyof typeof VEHICLE_TYPE_LABELS] || tipo;
  }

  /**
   * Obtener el label de un área
   */
  static getAreaLabel(area: string): string {
    return AREA_LABELS[area as keyof typeof AREA_LABELS] || area;
  }

  /**
   * Formatear fecha para mostrar
   */
  static formatDate(date: string | Date): string {
    const d = new Date(date);
    return d.toLocaleDateString('es-ES', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  }

  /**
   * Formatear fecha y hora para mostrar
   */
  static formatDateTime(date: string | Date): string {
    const d = new Date(date);
    return d.toLocaleString('es-ES', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  }

  /**
   * Formatear fecha para API (YYYY-MM-DD)
   */
  static formatDateForApi(date: Date): string {
    return date.toISOString().split('T')[0];
  }

  /**
   * Obtener el tiempo transcurrido desde una fecha
   */
  static getTimeElapsed(date: string | Date): string {
    const now = new Date();
    const past = new Date(date);
    const diffMs = now.getTime() - past.getTime();
    
    const diffMinutes = Math.floor(diffMs / (1000 * 60));
    const diffHours = Math.floor(diffMinutes / 60);
    const diffDays = Math.floor(diffHours / 24);

    if (diffDays > 0) {
      return `${diffDays} día${diffDays > 1 ? 's' : ''}`;
    } else if (diffHours > 0) {
      return `${diffHours} hora${diffHours > 1 ? 's' : ''}`;
    } else {
      return `${diffMinutes} minuto${diffMinutes > 1 ? 's' : ''}`;
    }
  }

  /**
   * Validar formato de placa colombiana
   */
  static isValidPlaca(placa: string): boolean {
    // Formato: 3 letras + 3 números (ej: ABC123)
    const placaRegex = /^[A-Z]{3}[0-9]{3}$/;
    return placaRegex.test(placa.toUpperCase());
  }

  /**
   * Validar formato de documento
   */
  static isValidDocumento(documento: string): boolean {
    // Solo números, entre 6 y 12 dígitos
    const docRegex = /^[0-9]{6,12}$/;
    return docRegex.test(documento);
  }

  /**
   * Generar nombre de archivo para exportación
   */
  static generateExportFilename(prefix: string = 'registros'): string {
    const now = new Date();
    const timestamp = now.toISOString().split('T')[0];
    return `${prefix}_${timestamp}.xlsx`;
  }

  /**
   * Obtener el color de Bootstrap según el área
   */
  static getAreaColor(area: string): string {
    const colorMap: { [key: string]: string } = {
      'produccion': 'primary',
      'administracion': 'secondary',
      'logistica': 'success',
      'soplado': 'warning'
    };
    return colorMap[area] || 'light';
  }

  /**
   * Obtener el icono según el tipo de vehículo
   */
  static getVehicleIcon(tipo: string): string {
    const iconMap: { [key: string]: string } = {
      'carro': '🚗',
      'moto': '🏍️',
      'bicicleta': '🚲'
    };
    return iconMap[tipo] || '🚗';
  }

  /**
   * Capitalizar primera letra de cada palabra
   */
  static capitalizeWords(text: string): string {
    return text.replace(/\w\S*/g, (txt) => 
      txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
    );
  }

  /**
   * Verificar si un vehículo está en el parqueadero
   */
  static isVehicleInParking(vehicle: any): boolean {
    return vehicle.active_registro !== null && vehicle.active_registro !== undefined;
  }
}


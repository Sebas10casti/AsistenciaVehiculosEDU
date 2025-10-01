import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

// Interfaces para tipado
export interface Vehicle {
  id?: number;
  tipo: string;
  nombre_dueno: string;
  documento: string;
  placa?: string;
  serial?: string;
  color: string;
  marca?: string;
  area: string;
  active_registro?: any;
}

export interface Registro {
  id?: number;
  vehiculo: number;
  dueño: string;
  placa_or_serial: string;
  fecha: string;
  hora_entrada: string;
  hora_salida?: string;
}

export interface ApiResponse<T> {
  data: T;
  message?: string;
  status: number;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  // ===== VEHÍCULOS =====
  
  /**
   * Obtener todos los vehículos
   */
  getVehicles(): Observable<Vehicle[]> {
    return this.http.get<Vehicle[]>(`${this.baseUrl}/vehicles/`);
  }

  /**
   * Obtener vehículo por ID
   */
  getVehicle(id: number): Observable<Vehicle> {
    return this.http.get<Vehicle>(`${this.baseUrl}/vehicles/${id}/`);
  }

  /**
   * Crear nuevo vehículo
   */
  createVehicle(vehicle: Vehicle): Observable<Vehicle> {
    return this.http.post<Vehicle>(`${this.baseUrl}/vehicles/`, vehicle);
  }

  /**
   * Actualizar vehículo
   */
  updateVehicle(id: number, vehicle: Vehicle): Observable<Vehicle> {
    return this.http.put<Vehicle>(`${this.baseUrl}/vehicles/${id}/`, vehicle);
  }

  /**
   * Eliminar vehículo
   */
  deleteVehicle(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/vehicles/${id}/`);
  }

  /**
   * Filtrar vehículos por tipo
   */
  getVehiclesByType(tipo: string): Observable<Vehicle[]> {
    const params = new HttpParams().set('tipo', tipo);
    return this.http.get<Vehicle[]>(`${this.baseUrl}/vehicles/`, { params });
  }

  /**
   * Registrar ingreso de vehículo
   */
  registerVehicleEntry(id: number): Observable<Registro> {
    return this.http.post<Registro>(`${this.baseUrl}/vehicles/${id}/ingreso/`, {});
  }

  /**
   * Registrar salida de vehículo
   */
  registerVehicleExit(id: number): Observable<Registro> {
    return this.http.post<Registro>(`${this.baseUrl}/vehicles/${id}/salida/`, {});
  }

  /**
   * Obtener historial de un vehículo
   */
  getVehicleHistory(id: number): Observable<Registro[]> {
    return this.http.get<Registro[]>(`${this.baseUrl}/vehicles/${id}/history/`);
  }

  // ===== REGISTROS =====

  /**
   * Obtener todos los registros
   */
  getRegistros(): Observable<Registro[]> {
    return this.http.get<Registro[]>(`${this.baseUrl}/registros/`);
  }

  /**
   * Obtener registros con filtros de fecha
   */
  getRegistrosByDate(desde?: string, hasta?: string): Observable<Registro[]> {
    let params = new HttpParams();
    if (desde) params = params.set('desde', desde);
    if (hasta) params = params.set('hasta', hasta);
    return this.http.get<Registro[]>(`${this.baseUrl}/registros/`, { params });
  }

  /**
   * Exportar registros a Excel
   */
  exportRegistros(desde?: string, hasta?: string): Observable<Blob> {
    let params = new HttpParams();
    if (desde) params = params.set('desde', desde);
    if (hasta) params = params.set('hasta', hasta);
    
    return this.http.get(`${this.baseUrl}/registros/export/`, {
      params,
      responseType: 'blob'
    });
  }

  // ===== UTILIDADES =====

  /**
   * Obtener vehículos actualmente en el parqueadero
   */
  getVehiclesInParking(): Observable<Vehicle[]> {
    return this.http.get<Vehicle[]>(`${this.baseUrl}/vehicles/`).pipe(
      // Filtrar solo vehículos con active_registro
      // Este filtro se puede hacer en el componente o crear un endpoint específico en el backend
    );
  }

  /**
   * Descargar archivo Excel
   */
  downloadFile(blob: Blob, filename: string): void {
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.click();
    window.URL.revokeObjectURL(url);
  }
}

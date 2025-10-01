import { Component, effect, inject } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { rxResource } from '@angular/core/rxjs-interop';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-vehicles-list',
  imports: [RouterLink],
  templateUrl: './vehicles-list.component.html',
})
export class VehiclesListComponent { 
private apiService = inject(ApiService);

public vehiclesResource = rxResource({
  stream: () => this.apiService.getVehicles(),
  defaultValue: []
});

public vehiclesResourceEffect = effect(() => {
  console.log(this.vehiclesResource.value());
});
}
